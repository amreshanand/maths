"""
Production Video Renderer, Audio Synchronizer, and Final Muxer
Orchestrates rendering all Manim scenes at 1080p 60fps, synchronizes narration,
mixes ambient background score, and exports output/Linear_Transformations_Final.mp4.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(PROJECT_ROOT))
from config import VIDEO_WIDTH, VIDEO_HEIGHT, FRAME_RATE, OUTPUT_DIR, AUDIO_DIR, MUSIC_DIR

SCENES = [
    {"id": "scene_01", "file": "src/scene_01_hook.py", "class": "Scene01Hook", "title": "Hook & Context"},
    {"id": "scene_02", "file": "src/scene_02_concept.py", "class": "Scene02Concept", "title": "Concept Definition"},
    {"id": "scene_03", "file": "src/scene_03_visual_intuition.py", "class": "Scene03VisualIntuition", "title": "Visual Intuition"},
    {"id": "scene_04", "file": "src/scene_04_worked_example.py", "class": "Scene04WorkedExample", "title": "Worked Example"},
    {"id": "scene_05", "file": "src/scene_05_interpretation.py", "class": "Scene05Interpretation", "title": "Interpretation"},
    {"id": "scene_06", "file": "src/scene_06_summary.py", "class": "Scene06Summary", "title": "Summary & Credits"},
]

def get_media_duration(file_path):
    """Returns the duration of an audio or video file in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def render_scenes_1080p(force_re_render=False):
    """Renders all scenes in 1080p at 60fps using Manim (or reuses existing renders)."""
    print("=" * 65)
    print("STEP 1: VERIFYING / RENDERING MANIM SCENES (1080p 60 FPS)")
    print("=" * 65)
    
    rendered_files = []
    for sc in SCENES:
        stem = Path(sc["file"]).stem
        expected_path = PROJECT_ROOT / "media" / "videos" / stem / f"{VIDEO_HEIGHT}p{FRAME_RATE}" / f"{sc['class']}.mp4"
        
        if not expected_path.exists() or force_re_render:
            print(f"\n>>> Rendering {sc['id']} ({sc['class']})...")
            cmd = [
                "manim", "-qh", "--fps", str(FRAME_RATE),
                sc["file"], sc["class"]
            ]
            subprocess.run(cmd, check=True)
            
        dur = get_media_duration(expected_path)
        print(f"✓ Ready: {sc['class']} ({dur:.2f}s) -> {expected_path.name}")
        rendered_files.append((sc["id"], expected_path, dur))
        
    return rendered_files

def sync_and_mux_scenes(rendered_scenes):
    """
    Synchronizes each rendered scene video with its calibrated narration audio.
    Aligns lengths cleanly: clamps or holds frame precisely for narration completion.
    """
    print("\n" + "=" * 65)
    print("STEP 2: SYNCHRONIZING NARRATION WITH VIDEO SCENES")
    print("=" * 65)
    
    synced_clips = []
    tmp_dir = PROJECT_ROOT / "media" / "synced_scenes"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    
    for scene_id, video_path, v_dur in rendered_scenes:
        audio_path = AUDIO_DIR / f"{scene_id}.mp3"
        if not audio_path.exists():
            raise FileNotFoundError(f"Missing audio file: {audio_path}")
            
        a_dur = get_media_duration(audio_path)
        out_clip = tmp_dir / f"{scene_id}_synced.mp4"
        print(f">>> Syncing {scene_id}: Video={v_dur:.2f}s, Audio={a_dur:.2f}s")
        
        # Target duration ensures audio plays completely without abrupt cut
        target_dur = max(v_dur, a_dur + 0.3)
        
        cmd = [
            "ffmpeg", "-y",
            "-i", str(video_path),
            "-i", str(audio_path),
            "-filter_complex",
            f"[0:v]tpad=stop_mode=clone:stop_duration={target_dur:.2f}[v];[1:a]apad[a]",
            "-map", "[v]",
            "-map", "[a]",
            "-t", f"{target_dur:.2f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FRAME_RATE),
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
            str(out_clip)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        actual_dur = get_media_duration(out_clip)
        print(f"✓ Synced {scene_id} -> {actual_dur:.2f}s ({out_clip.name})")
        synced_clips.append(out_clip)
        
    return synced_clips

def assemble_final_video(synced_clips):
    """
    Concatenates synced scenes and mixes subtle background music.
    Produces final submission video in output/Linear_Transformations_Final.mp4.
    """
    print("\n" + "=" * 65)
    print("STEP 3: CONCATENATING SCENES & MIXING BACKGROUND MUSIC")
    print("=" * 65)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    final_output = OUTPUT_DIR / "Linear_Transformations_Final.mp4"
    
    concat_list = PROJECT_ROOT / "media" / "concat_list.txt"
    with open(concat_list, "w") as f:
        for clip in synced_clips:
            f.write(f"file '{clip.resolve()}'\n")
            
    tmp_assembled = PROJECT_ROOT / "media" / "assembled_narration.mp4"
    
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(tmp_assembled)
    ]
    subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    total_dur = get_media_duration(tmp_assembled)
    print(f"✓ Assembled narration cut: {total_dur:.2f}s ({total_dur/60:.2f} mins)")
    
    music_file = MUSIC_DIR / "ambient_math_score.wav"
    if not music_file.exists():
        raise FileNotFoundError(f"Music file not found: {music_file}")
        
    print(f">>> Mixing ambient background music at subtle level (-22 dB / volume 0.08)...")
    
    fade_start = max(0.0, total_dur - 4.0)
    cmd_mix = [
        "ffmpeg", "-y",
        "-i", str(tmp_assembled),
        "-stream_loop", "-1", "-i", str(music_file),
        "-filter_complex",
        f"[0:a]volume=1.0[narr];"
        f"[1:a]volume=0.08,afade=t=in:st=0:d=3,afade=t=out:st={fade_start:.2f}:d=4[bg];"
        f"[narr][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-t", f"{total_dur:.2f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        str(final_output)
    ]
    subprocess.run(cmd_mix, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    final_dur = get_media_duration(final_output)
    file_size_mb = final_output.stat().st_size / (1024 * 1024)
    
    print("\n" + "=" * 65)
    print(f"★ FINAL DELIVERABLE VIDEO READY!")
    print(f"★ Location:   {final_output}")
    print(f"★ Duration:   {final_dur:.2f} seconds ({final_dur/60:.2f} minutes)")
    print(f"★ Resolution: {VIDEO_WIDTH}x{VIDEO_HEIGHT} @ {FRAME_RATE} fps")
    print(f"★ File Size:  {file_size_mb:.2f} MB")
    print("=" * 65)
    return final_output

def main():
    rendered_scenes = render_scenes_1080p()
    synced_clips = sync_and_mux_scenes(rendered_scenes)
    final_video = assemble_final_video(synced_clips)
    return final_video

if __name__ == "__main__":
    main()

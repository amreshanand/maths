"""
Procedural Background Music Generator
Generates a warm, subtle, minimalist ambient math soundbed (royalty-free / CC0)
Uses pure NumPy and scipy.io.wavfile to construct multi-layered ambient chords with slow ADSR envelopes.
"""

import numpy as np
import scipy.io.wavfile as wavfile
from pathlib import Path

def generate_ambient_music(output_path, duration_seconds=360, sample_rate=44100):
    """
    Generates a continuous calm ambient pad soundtrack.
    Progression: Cmaj9 -> Fmaj7 -> Am9 -> Gsus4 (gentle, reflective academic tone).
    """
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)
    audio = np.zeros_like(t)

    # Chords in Hz: (root, 3rd, 5th, 7th/9th)
    # Cmaj9: C3 (130.81), E3 (164.81), G3 (196.00), B3 (246.94), D4 (293.66)
    # Fmaj7: F2 (87.31), C3 (130.81), E3 (164.81), A3 (220.00)
    # Am9: A2 (110.00), E3 (164.81), G3 (196.00), C4 (261.63), B3 (246.94)
    # Gsus4: G2 (98.00), D3 (146.83), G3 (196.00), C4 (261.63)

    chord_progression = [
        [130.81, 164.81, 196.00, 246.94, 293.66],  # Cmaj9
        [87.31, 130.81, 164.81, 220.00, 329.63],   # Fmaj7
        [110.00, 164.81, 196.00, 246.94, 261.63],  # Am9
        [98.00, 146.83, 196.00, 261.63, 293.66],   # Gsus4
    ]

    chord_duration = 10.0  # 10 seconds per chord
    total_chords = int(np.ceil(duration_seconds / chord_duration))

    for i in range(total_chords):
        c_idx = i % len(chord_progression)
        freqs = chord_progression[c_idx]
        start_t = i * chord_duration
        end_t = min((i + 1) * chord_duration + 3.0, duration_seconds)  # 3-sec overlap for seamless crossfade
        
        idx_start = int(start_t * sample_rate)
        idx_end = int(end_t * sample_rate)
        seg_len = idx_end - idx_start
        if seg_len <= 0:
            continue
            
        t_seg = np.linspace(0, end_t - start_t, seg_len, endpoint=False)
        
        # Smooth Hann-like window for fade in/out
        fade_len = int(2.5 * sample_rate)
        env = np.ones(seg_len)
        if seg_len > 2 * fade_len:
            env[:fade_len] = 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, fade_len)))
            env[-fade_len:] = 0.5 * (1 + np.cos(np.pi * np.linspace(0, 1, fade_len)))
        else:
            env = np.sin(np.pi * np.linspace(0, 1, seg_len))

        # Synthesize chord layers with soft harmonics
        chord_wave = np.zeros(seg_len)
        for f in freqs:
            # Fundamental
            chord_wave += 0.5 * np.sin(2 * np.pi * f * t_seg)
            # Soft 2nd harmonic (octave)
            chord_wave += 0.2 * np.sin(2 * np.pi * (f * 2.0) * t_seg)
            # Soft 3rd harmonic (fifth)
            chord_wave += 0.08 * np.sin(2 * np.pi * (f * 3.0) * t_seg)

        # Gentle LFO (low frequency oscillation) for organic warmth
        lfo = 1.0 + 0.15 * np.sin(2 * np.pi * 0.2 * t_seg)
        chord_wave = chord_wave * env * lfo
        
        audio[idx_start:idx_end] += chord_wave

    # Add subtle sub-bass warmth (55 Hz / 65 Hz)
    sub = 0.15 * np.sin(2 * np.pi * 55.0 * t) * (1.0 + 0.1 * np.sin(2 * np.pi * 0.1 * t))
    audio += sub

    # Normalize audio to prevent clipping and keep peak at -12 dB (subtle background level)
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio / peak * 0.25  # Soft background level

    # Convert to 16-bit PCM
    audio_int16 = (audio * 32767).astype(np.int16)

    # Save WAV
    out_p = Path(output_path)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(str(out_p), sample_rate, audio_int16)
    print(f"✓ Background music successfully generated: {out_p} ({duration_seconds}s)")

if __name__ == "__main__":
    generate_ambient_music("assets/music/ambient_math_score.wav", duration_seconds=360)

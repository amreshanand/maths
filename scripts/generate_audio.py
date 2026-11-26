"""
Narration Audio Generator (Calibrated for ~5 minutes runtime)
Generates high quality neural voiceover for all 6 scenes using Edge-TTS (with fallback to macOS 'say')
Tuned to align smoothly with 1080p Manim animations.
"""

import asyncio
import os
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(PROJECT_ROOT))
from config import STUDENT_NAME, STUDENT_ID

SCENE_SCRIPTS = {
    "scene_01": (
        f"Have you ever wondered how computer graphics rotate a 3D character, how game engines warp space, "
        f"or how physics models coordinate systems? "
        f"At the very heart of these technologies lies the linear transformation. "
        f"A matrix is not just a spreadsheet of numbers—it is a geometric engine that stretches, rotates, shears, and reshapes space. "
        f"Welcome to Linear Transformations: How Matrices Transform 2D Space. "
        f"I am {STUDENT_NAME}, Student ID {STUDENT_ID}. "
        f"Let us explore how matrices transform space, why basis vectors hold the key to everything, "
        f"and how to visualize the geometry behind the algebra."
    ),
    "scene_02": (
        "Let us begin with first principles. What is a transformation? "
        "In mathematics, a transformation is simply a function—a rule mapping an input vector v to an output vector T of v. "
        "When linear, it is computed through matrix multiplication: T of v equals A times v. "
        "To be strictly linear, it must satisfy two axioms. "
        "First, additivity: transforming the sum of two vectors must equal the sum of their individual transformations: "
        "T of u plus v equals T of u plus T of v. Geometrically, vector addition parallelograms stay intact. "
        "Second, homogeneity: scaling a vector by a constant c and then transforming it gives the same result as "
        "transforming first and scaling after: T of c times u equals c times T of u. "
        "Crucially, these two properties mandate that the origin must remain fixed: T of zero equals zero. "
        "If a transformation displaces the origin, it is an affine shift, not a linear transformation. "
        "In a linear world, grid lines remain straight and parallel, and the origin never moves."
    ),
    "scene_03": (
        "How do we visualize what a matrix does to every point in the 2D plane? "
        "The secret lies in the standard basis vectors: e one equals one zero along the x-axis, and e two equals zero one along the y-axis. "
        "Every vector in two dimensions is a linear combination of these basis vectors: x times e one plus y times e two. "
        "Because the transformation is linear, wherever e one and e two land completely determines where every other vector must go! "
        "Look at our matrix A: two, one; one, two. "
        "The first column reveals that e one lands at two, one. "
        "The second column reveals that e two lands at one, two. "
        "Now watch the coordinate grid transform smoothly. As basis vectors move to their targets, the entire grid deforms in unison. "
        "The original unit square morphs into a parallelogram whose vertices are zero zero, two one, three three, and one two. "
        "The matrix columns are literally the landing coordinates of our unit basis vectors!"
    ),
    "scene_04": (
        "Let us verify this algebraically with concrete examples. "
        "Our transformation rule is T of x, y equals two x plus y, and x plus two y. "
        "Consider our first vector: v one equals one, one, the diagonal of our original unit square. "
        "Multiplying by matrix A: the top component is two times one plus one times one, which equals three. "
        "The bottom component is one times one plus two times one, which also equals three. "
        "So, A times one, one equals three, three. "
        "Geometrically, v one expands directly along its diagonal to the tip of our parallelogram at three, three. "
        "Next, test a second vector: v two equals two, negative one. "
        "Multiplying by A: the top component is two times two plus one times negative one, which is four minus one, equaling three. "
        "The bottom component is one times two plus two times negative one, which is two minus two, equaling zero. "
        "Thus, A times two, negative one equals three, zero. "
        "Notice how v two has rotated and stretched to land precisely on the horizontal x-axis at three, zero! "
        "Algebra and geometry align in complete harmony."
    ),
    "scene_05": (
        "What does a matrix do to the space as a whole? "
        "First, consider the determinant of A. "
        "It is calculated as two times two minus one times one, which is four minus one, equaling three. "
        "The absolute value of the determinant is the area scaling factor of the transformation. "
        "Our original unit square had an area of one; the transformed parallelogram has an area of exactly three. "
        "Because the determinant is positive, spatial orientation is preserved. "
        "Next, notice that different directions stretch differently. "
        "Along direction one, one, vectors do not turn; they stretch by a factor of three. This is an eigenvector with eigenvalue three. "
        "Along direction one, negative one, vectors also do not turn, and their length is preserved: eigenvalue one. "
        "Finally, consider a critical distinction: does preserving area mean a transformation is a rotation? "
        "Look at matrix B equals two, zero; zero, zero point five. Its determinant is one, so area is preserved. "
        "Yet it is not a rigid rotation! Horizontal lengths doubled while vertical lengths halved. "
        "Determinant one guarantees area preservation, but not distance preservation."
    ),
    "scene_06": (
        "To summarize our journey: "
        "First, a 2D linear transformation preserves straight parallel lines and anchors the origin. "
        "Second, matrix columns directly represent where basis vectors e one and e two land. "
        "Third, the determinant measures area scaling, with positive values preserving orientation. "
        "Fourth, eigenvectors reveal invariant directions where the transformation acts as pure scaling. "
        "And fifth, area preservation does not imply distance preservation. "
        "Thank you for watching this presentation of the M3 Mathematics Animation Video Project. "
        f"Created by {STUDENT_NAME}, Student ID {STUDENT_ID}."
    )
}

VOICE = "en-US-ChristopherNeural"
RATE = "+26%"  # Perfectly paced instructional delivery (~155 words/min)
OUTPUT_AUDIO_DIR = PROJECT_ROOT / "assets" / "audio"

async def generate_scene_audio_edge(scene_id, text, output_file):
    import edge_tts
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, volume="+0%")
    await communicate.save(str(output_file))

def generate_scene_audio_mac_say(text, output_file):
    aiff_tmp = output_file.with_suffix(".aiff")
    subprocess.run(["say", "-v", "Samantha", "-r", "200", "-o", str(aiff_tmp), text], check=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(aiff_tmp), 
        "-c:a", "libmp3lame", "-b:a", "192k", str(output_file)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if aiff_tmp.exists():
        aiff_tmp.unlink()

async def main():
    OUTPUT_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    print("=" * 60)
    print("GENERATING CALIBRATED NARRATION AUDIO TRACKS")
    print("=" * 60)
    
    for scene_id, script in SCENE_SCRIPTS.items():
        out_mp3 = OUTPUT_AUDIO_DIR / f"{scene_id}.mp3"
        print(f"Generating voiceover for {scene_id} at {RATE}...")
        try:
            await generate_scene_audio_edge(scene_id, script, out_mp3)
            print(f"✓ Generated {out_mp3.name} using Edge-TTS ({VOICE})")
        except Exception as e:
            print(f"! Edge-TTS failed ({e}), falling back to macOS 'say'...")
            generate_scene_audio_mac_say(script, out_mp3)
            print(f"✓ Generated {out_mp3.name} using macOS voice")

    print("\n✓ All 6 scene audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())

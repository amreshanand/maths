"""
Main Application Entry Point for M3 Linear Transformations Project
Usage:
    python src/main.py --all       # Run tests, audio generation, and full 1080p rendering
    python src/main.py --verify    # Run mathematical verification suite
    python src/main.py --render    # Render scenes and generate final video
"""

import sys
import argparse
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(PROJECT_ROOT))

from tests.verify_transformations import run_all_tests
from scripts.render_and_mux import main as run_render_pipeline

def main():
    parser = argparse.ArgumentParser(description="M3 Mathematics Animation Video Pipeline")
    parser.add_argument("--verify", action="store_true", help="Run mathematical verification test suite")
    parser.add_argument("--render", action="store_true", help="Render all 1080p scenes and mux final video")
    parser.add_argument("--all", action="store_true", help="Run full pipeline: verification, audio, and rendering")

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.all:
        print("\n>>> [1/3] Running Mathematical Verification Suite...")
        run_all_tests()
        print("\n>>> [2/3] Rendering Full 1080p Video & Muxing Soundtrack...")
        run_render_pipeline()
        print("\n★ Full pipeline completed successfully!")
    elif args.verify:
        run_all_tests()
    elif args.render:
        run_render_pipeline()

if __name__ == "__main__":
    main()

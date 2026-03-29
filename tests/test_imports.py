import pytest
import os
import sys

# Add source directory to path to allow importing qtube
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'source'))

def test_imports():
    """Test that all required dependencies are present and can be imported."""
    import pytube
    import yt_dlp
    import PySide6
    from PySide6 import QtWidgets, QtCore, QtGui

    # Try importing modules from the source
    import texts_for_UI
    # We won't import YouTubePlayer from qtube here because it initializes Qt
    # which might fail in headless environments without additional setup.

def test_yt_dlp_availability():
    """Test if yt-dlp is correctly installed and accessible."""
    from yt_dlp import YoutubeDL
    ydl = YoutubeDL()
    assert ydl is not None

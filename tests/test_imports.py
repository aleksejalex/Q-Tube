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

    # Check that they are not none
    assert pytube is not None
    assert yt_dlp is not None
    assert PySide6 is not None
    assert QtWidgets is not None
    assert QtCore is not None
    assert QtGui is not None
    assert texts_for_UI is not None


def test_yt_dlp_availability():
    """Test if yt-dlp is correctly installed and accessible."""
    from yt_dlp import YoutubeDL
    ydl = YoutubeDL()
    assert ydl is not None

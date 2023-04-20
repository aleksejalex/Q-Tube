# TODO notes

## Problems:
 - sometimes there is a lag between pressing 'Download' button and
    open file dialog
 - after download starts, whole UI freezes (Not responding) until download completes. 
    Hypothesis: it happens because both video downloader and UI runs on single thread.
 - 

## To implement:
 - error handling: what downloader will do, if user enters some mess instead of YouTube link?
 - progress bar during downloading of the video
 - draw my own icon
 - function `self.offer_streams`: show list of streams with description,
    and make possible to get stream id via `clicked()`
 - add possibility to press `return` when in `textEdit`

## To test:
 - 
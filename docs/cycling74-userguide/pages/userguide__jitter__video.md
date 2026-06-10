---
title: "Video"
source: https://docs.cycling74.com/userguide/jitter/video/
source_path: /userguide/jitter/video/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Video

Source: https://docs.cycling74.com/userguide/jitter/video/

## Extracted Text

# Video
The Jitter video engine supports streaming video from a webcam or other video capture device, as well as playing a video from disk. Using the third party Syphon and Spout packages, it's also possible to stream video to other applications.
For applications like random video access or rapid resequencing of video material, you might want to consider loading your video into memory, or using a specially designed encoding like HAP .
## Playing a Video File
Use the jit.movie object to stream a video from disk. This object uses the current video engine to manage reading and streaming the video.
The standard jit.movie object plays back audio directly using the video engine, rather than routing audio through Max. Use the jit.movie~ object to use the audio tracks of the video file in Max. The mc.jit.movie~ file makes the audio tracks available as multichannel audio.
### Random Access
Use the`rate`message to change the playback speed of a jit.movie object. Use the`frame`and`jump`messages to move between different parts of the video file.
Keep in mind that videos files are generally encoded in a way that optimizes linear playback from start to finish. Depending on the size of the video file, your computer, and the specifications of your hard drive, you might need to make a couple of changes to improve performance when jumping around a video file.
When using the viddll engine, you can use the`loadram`message to pull an entire video file into Max's application memory. Accessing application memory can be significantly faster than accessing hard disk memory, and this might improve performance.
The HAP codec (collection of codecs actually) is a specially designed video encoding that's made for VJs and creative codeers. Depending on how you're using your video in Max, you might find that jit.movie is more responsive when using the HAP codec.
## Using a Video Capture Device
The jit.grab object manages access to video capture devices. Use the`open`and`close`messages to get access to a particular capture device. The`getvdevlist`and`getformatlist`messages let you fetch a list of capture devices and formats, which you can set with the`vdevice`and`format`messages. Check the jit.grab helpfile for more details.
## Recording
Max gives you a lot of flexibility when it comes to recording video, but there are three general approaches: using jit.record/jit.vcr, using Syphon or Spout to send video to an external recorder like OBS , or frame-by-frame export with jit.matrix and`exportimage`.
### Recording with jit.record and jit.vcr
The jit.record and jit.vcr objects let you record a stream of Jitter matrices to disk. In terms of video recording the two objects are the same, except jit.vcr can record audio as well as video. This is the simplest and most straightforward way to record video. For higher quality recording, consider recording with Syphon, Spout, and OBS .
You can use the`@codec`attribute to change the codec used for recording, from`prores444`for a high quality recording with alpha, to`h264`for a lossy encoding and a smaller file size. The jit.record object can record frames as it receives them (non-realtime mode, the default), in which case you'll need to be sure that your recording FPS (frame per second) matches the FPS of your Jitter patcher. Finally, note that jit.record and jit.vcr both record matrices, not Jitter textures . If you want to record a texture, use jit.gl.asyncread to convert textures to matrices.
The jit.gl.asyncread object converts textures to matrices for recording
### Recording with Syphon, Spout, and OBS
If you want to make a higher quality recording, often it's better to send textures through Syphon or Spout to an external application like OBS . After installing Syphon or Spout , create the apporpriate server object:`jit.gl.syphonserver`for Syphon, and`jit.gl.spoutsender`for Spout. If you're using jit.world , enable the`@output_texture`attribute to make sure that jit.world is sending its texture as an output.
If you're using jit.world , you'll need to make sure that the texture size coming out of jit.world matches what OBS is expectind to record. Set the`@dim`attribute to match the canvas resolution in OBS. You'll also need to include a`jit.gl.camera`object in your patcher, to make the viewport size independent of the`jit.world`window size.
Copy
Using jit.gl.syphonserver to send textures from Max to OBS
To record audio as well as video, create a new Audio Capture source in OBS, and configure this for Application Capture. Set the application to Max, and you can record audio from Max at the same time as you record video.
A simple OBS setup for recording video with audio from Max
OBS audio sources may not support Application Capture on Windows. You can use Desktop Capture, or you can use a third-party application to route audio from Max to OBS. We recommend Voicemeeter or JACK .
### Recording with frame-by-frame with jit.matrix and`exportimage`
For total control over the recording process, you can explore a non-realtime recording setup. This will look something like the digital equivalent of stop motion filmmaking. After rendering your scene, capture the output in a jit.matrix object. Send that object the`exportimage`message to save the image to disk. Later, use FFmpeg to render a final video from your sequence of images.
## Further Reading
For a more in-depth tutorial concerning recording video from Max, check out this article .

import { useEffect, useRef, useState } from "react";

function UploadSection({ onDetect }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);

  const canvasRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);
  const timerRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setSelectedFile(file);
      drawWaveform(file);
    }
  };

  const drawWaveform = async (file) => {
    try {
      const arrayBuffer = await file.arrayBuffer();

      const audioContext = new AudioContext();
      const audioBuffer =
        await audioContext.decodeAudioData(arrayBuffer);

      const channelData = audioBuffer.getChannelData(0);

      const canvas = canvasRef.current;

      if (!canvas) {
        await audioContext.close();
        return;
      }

      const ctx = canvas.getContext("2d");

      const width = canvas.width;
      const height = canvas.height;

      ctx.clearRect(0, 0, width, height);

      ctx.beginPath();

      const step = Math.ceil(channelData.length / width);

      for (let x = 0; x < width; x++) {
        let min = 1;
        let max = -1;

        const start = x * step;
        const end = Math.min(
          start + step,
          channelData.length
        );

        for (let i = start; i < end; i++) {
          const value = channelData[i];

          if (value < min) min = value;
          if (value > max) max = value;
        }

        const y1 = ((1 + min) / 2) * height;
        const y2 = ((1 + max) / 2) * height;

        ctx.moveTo(x, y1);
        ctx.lineTo(x, y2);
      }

      ctx.stroke();

      await audioContext.close();

    } catch (error) {
      console.error("Waveform error:", error);
    }
  };

  const startRecording = async () => {
    try {
      const stream =
        await navigator.mediaDevices.getUserMedia({
          audio: true,
        });

      const mediaRecorder = new MediaRecorder(stream);

      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(
          audioChunksRef.current,
          {
            type: mediaRecorder.mimeType,
          }
        );

        const recordedFile = new File(
          [audioBlob],
          "Microphone_Recording.webm",
          {
            type: mediaRecorder.mimeType,
          }
        );

        console.log(
          "Recording created:",
          recordedFile.name,
          recordedFile.type,
          recordedFile.size
        );

        setSelectedFile(recordedFile);

        drawWaveform(recordedFile);

        stream
          .getTracks()
          .forEach((track) => track.stop());
      };

      mediaRecorder.start();

      setIsRecording(true);
      setRecordingTime(0);

      timerRef.current = setInterval(() => {
        setRecordingTime((time) => time + 1);
      }, 1000);

    } catch (error) {
      console.error(
        "Microphone error:",
        error
      );

      alert(
        "Microphone permission is required."
      );
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
    }

    setIsRecording(false);

    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  };

  const handleDetect = () => {
    if (selectedFile) {
      onDetect(selectedFile);
    }
  };

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }
    };
  }, []);

  return (
    <section className="upload-section">

      <h2>Upload Audio File</h2>

      <div className="upload-box">

        <p>🎵 Select your audio file</p>

        <input
          type="file"
          accept=".wav,.mp3"
          onChange={handleFileChange}
        />

        <div className="record-section">

          <p>🎙️ Or record your voice</p>

          {!isRecording ? (
            <button
              className="record-btn"
              onClick={startRecording}
            >
              🎙️ Start Recording
            </button>
          ) : (
            <button
              className="stop-btn"
              onClick={stopRecording}
            >
              ⏹️ Stop Recording
            </button>
          )}

          {isRecording && (
            <p className="recording-status">
              🔴 Recording... {recordingTime}s
            </p>
          )}

        </div>

        {selectedFile && (
          <div className="audio-preview">

            <p>
              🎧 Selected:{" "}
              <strong>
                {selectedFile.name}
              </strong>
            </p>

            <audio
              controls
              src={URL.createObjectURL(selectedFile)}
              className="audio-player"
            />

            <h3>🎚️ Audio Waveform</h3>

            <canvas
              ref={canvasRef}
              width="900"
              height="180"
              className="waveform-canvas"
            />

          </div>
        )}

        <button
          className="upload-btn"
          onClick={handleDetect}
          disabled={
            !selectedFile || isRecording
          }
        >
          🔍 Detect Deepfake
        </button>

      </div>

    </section>
  );
}

export default UploadSection;
import tkinter as tk
from tkinter import messagebox, filedialog
import pyaudio
import wave
import threading
import os

# --- Configuration Constants ---
FORMAT = pyaudio.paInt16
CHANNELS = 1
fs = 44100
CHUNK = 1024

# --- Global State Variables ---
is_recording = False
frames = []
p = None
stream = None
seconds_elapsed = 0

# --- Functions ---

def record_audio_loop():
    """Background hardware audio capture loop."""
    global is_recording, frames, p, stream
    
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=fs,
        input=True,
        frames_per_buffer=CHUNK
    )

    while is_recording:
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
        except Exception as e:
            print(f"Error recording audio: {e}")
            break

    # Stop hardware streams
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Safe return execution back to the main UI thread
    root.after(0, save_audio_file)

def update_timer():
    """Schedules continuous visual clock ticks."""
    global seconds_elapsed, is_recording
    if is_recording:
        seconds_elapsed += 1
        minutes = seconds_elapsed // 60
        seconds = seconds_elapsed % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        # Run again in 1 second
        root.after(1000, update_timer)

def save_audio_file():
    """Handles exporting memory buffers to disk storage."""
    global frames, p
    file_path = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[("Wave Audio Files", "*.wav"), ("All Files", "*.*")],
        title="Save Recording"
    )
    
    if file_path:
        try:
            wf = wave.open(file_path, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(fs)
            wf.writeframes(b''.join(frames))
            wf.close()
            messagebox.showinfo("Success", f"Audio saved to:\n{os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")
    else:
        messagebox.showwarning("Cancelled", "Recording discarded.")
        
    # Reset UI State
    status_label.config(text="Ready to Record", fg="#94A3B8")
    timer_label.config(text="00:00")

def toggle_recording():
    """Starts or stops the recorder based on current execution state."""
    global is_recording, frames, seconds_elapsed
    
    if not is_recording:
        # Start State
        is_recording = True
        frames = []
        seconds_elapsed = 0
        
        status_label.config(text="Recording...", fg="#EF4444")
        record_btn.config(text="🛑 Stop Recording", bg="#EF4444", activebackground="#DC2626")
        
        # Fire background thread
        audio_thread = threading.Thread(target=record_audio_loop, daemon=True)
        audio_thread.start()
        update_timer()
    else:
        # Stop State
        is_recording = False
        status_label.config(text="Saving file...", fg="#EAB308")
        record_btn.config(text="🎤 Start Recording", bg="#10B981", activebackground="#059669")

# --- Interface Setup ---
root = tk.Tk()
root.title("Python Voice Recorder")
root.geometry("350x250")
root.configure(bg="#0F172A")

# Status UI Component
status_label = tk.Label(
    root, 
    text="Ready to Record", 
    font=("Arial", 14, "bold"), 
    bg="#0F172A", 
    fg="#94A3B8"
)
status_label.pack(pady=20)

# Timer UI Component
timer_label = tk.Label(
    root, 
    text="00:00", 
    font=("Courier", 30, "bold"), 
    bg="#0F172A", 
    fg="#F8FAFC"
)
timer_label.pack(pady=10)

# Command Action Button
record_btn = tk.Button(
    root, 
    text="🎤 Start Recording", 
    font=("Arial", 12, "bold"),
    bg="#10B981", 
    fg="black", 
    activebackground="#059669",
    padx=20, 
    pady=10, 
    command=toggle_recording,
    relief="flat"
)
record_btn.pack(pady=20)

root.mainloop()

frame_time = start_time + timedelta(seconds=frame_idx / camera_fps)
        timestamp_str = frame_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        camera_timestamps.append((f"frame_{frame_idx:06d}.jpg", timestamp_str))
        cv2.imwrite(os.path.join(output_frame_dir, f"frame_{frame_idx:06d}.jpg"), frame)
        cam_ts_file.write(f"{timestamp_str}\n")
        frame_idx += 1

sync_pairs = []
for i, lidar_time in enumerate(lidar_times):
    time_diffs = [abs((lidar_time - cam_time).total_seconds()) for cam_time in camera_times]
    closest_cam_idx = time_diffs.index(min(time_diffs))
    sync_pairs.append((i, closest_cam_idx))

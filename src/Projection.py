frame_size = None

for lidar_idx, cam_idx in synced_pairs:
    # Load point cloud
    pcd_path = os.path.join(lidar_folder, f"video_big1 (Frame {lidar_idx}).pcd")
    if not os.path.exists(pcd_path):
        print(f"⚠️ Missing LiDAR file: {pcd_path}")
        continue

    pcd = o3d.io.read_point_cloud(pcd_path)
    points = np.asarray(pcd.points)

    if hasattr(pcd, 'intensities'):
        intensities = np.asarray(pcd.intensities)
    elif pcd.has_colors():
        intensities = np.asarray(pcd.colors)[:, 0] * 255
    else:
        intensities = np.zeros(len(points))  # fallback

    cam_path = os.path.join(camera_folder, f"frame_{cam_idx:06d}.jpg")
    image = cv2.imread(cam_path)
    if image is None:
        print(f"❌ Missing frame: {cam_path}")
        continue

    if frame_size is None:
        frame_size = (image.shape[1], image.shape[0])

    pts_2d, distances, intensities = project_lidar_to_image(points, intensities, R, T, K, dist_coeffs)

    if len(distances) > 0:
        min_d, max_d = distances.min(), distances.max()
    else:
        continue

    for pt, d in zip(pts_2d, distances):
        x, y = int(pt[0]), int(pt[1])
        if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
            norm_d = (d - min_d) / (max_d - min_d + 1e-5)
            rgb_color = get_vibgyor_color(norm_d)  # RGB
            bgr_color = cv2.cvtColor(np.uint8([[rgb_color]]), cv2.COLOR_RGB2BGR)[0, 0].tolist()
            cv2.circle(image, (x, y), 2, bgr_color, -1)

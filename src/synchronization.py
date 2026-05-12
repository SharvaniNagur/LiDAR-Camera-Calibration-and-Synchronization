frame_size = None

for lidar_idx, cam_idx in synced_pairs:
    pcd_path = os.path.join(lidar_folder, f"video_big1 (Frame {lidar_idx}).pcd")
    pcd = o3d.io.read_point_cloud(pcd_path)
    points = np.asarray(pcd.points)
    cam_path = os.path.join(camera_folder, f"frame_{cam_idx:06d}.jpg")
    image = cv2.imread(cam_path)
    if image is None:
        print(f"❌ Missing frame: {cam_path}")
        continue
    if frame_size is None:
        frame_size = (image.shape[1], image.shape[0])
    pts_2d = project_lidar_to_image(points, R, T, K, dist_coeffs)

    for pt in pts_2d:
        x, y = int(pt[0]), int(pt[1])
        if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)


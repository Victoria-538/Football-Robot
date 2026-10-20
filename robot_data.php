
<?php
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$connect = mysqli_connect(
    'localhost',
    'victoria',
    '*****',
    'football_robot'
);

if (!$connect) {
    http_response_code(500);
    echo json_encode(['error' => 'Database connection failed']);
    exit;
}

$query = "SELECT time, state, direction, acceleration, speed
          FROM robot_status
          ORDER BY time DESC, id DESC
          LIMIT 1";

$result = mysqli_query($connect, $query);

if (!$result) {
    http_response_code(500);
    echo json_encode(['error' => 'Database query failed']);
    mysqli_close($connect);
    exit;
}

$record = mysqli_fetch_assoc($result);

echo json_encode($record ?: []);

mysqli_close($connect);
?>

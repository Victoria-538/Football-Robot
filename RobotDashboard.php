
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST"
    && isset($_POST['start'])) {

 shell_exec(
        "/usr/bin/python3 /var/www/html/robot_command.py START"
    );

    $message = "START command sent";
} else {
    $message = "Robot is idle";
}
?>

				
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Football Robot Dashboard</title>
    <style>
		body {
			font-family: Arial, sans-serif;
			background-color: #f1f3f5;
			margin: 20px;
		}
		h1 {
			text-align: center;
		}
		.dashboard {
			display:grid;
			grid-template-columns: 1fr 1.5fr;
			gap: 20px;
		}
		.panel {
			background-color: white;
			padding: 20px;
			border-radius: 10px;
		}
		
		.panelh2{
			margin-top:0;
			color: #343a40;
			border-bottom: 2px solid #dee2e6;
			padding-bottom: 10px;
		}
		.panel p {
			padding: 10px;
			margin: 8px 0;
			background-color: #f8f9fa;
			border-radius: 5px;
		}

		.panel strong {
			display: inline-block;
			width: 120px;
			color: #495057;
		}
				
		.start-button {
			display: block;
			margin: 20px auto;
			padding: 12px 30px;
			background-color: #198754;
			color: white;
			border: none;
			border-radius: 8px;
			font-size: 16px;
			cursor: pointer;
		}

		.start-button:hover {
			background-color: #146c43;
		}

    </style>
</head>
<body>
    <h1>Football Robot Dashboard</h1>
	<form method="post" action="">
		<button class="start-button"
            type="submit"
            name="start"
            value="1">
        Start Robot
		</button>
	</form>

<p style="text-align: center;">
    <?php echo htmlspecialchars($message); ?>
</p>


    <div class="dashboard">
		<div class="panel">
			 <h2>Robot Data</h2>

			 <p><strong>Time:</strong> <span id="robot-time">Loading...</span></p>
			 <p><strong>State:</strong> <span id="robot-state">Loading...</span></p>
			 <p><strong>Direction:</strong> <span id="robot-direction">Loading...</span></p>
			 <p><strong>Acceleration:</strong> <span id="robot-acceleration">Loading...</span></p>
			 <p><strong>Speed:</strong> <span id="robot-speed">Loading...</span></p>

			 <p id="data-status" style="font-size: 12px;">
			 Connecting to database...
			 </p>
		</div>
		<div class="panel">
			<h2>Football Robot</h2>
			 <img
				src="images/robot.jpg"
				alt="Football robot camera placeholder"
				style="
					display: block;
					width: 100%;
					height: auto;
					border-radius: 5px;
					background: #000;
				"
			>
			
		</div>
    </div>

<script>
async function updateRobotData() {
    const status = document.getElementById('data-status');

    try {
        const response = await fetch('robot_data.php?t=' + Date.now(), {
            cache: 'no-store'
        });

        if (!response.ok) {
            throw new Error('HTTP ' + response.status);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        const fields = {
            'robot-time': 'time',
            'robot-state': 'state',
            'robot-direction': 'direction',
            'robot-acceleration': 'acceleration',
            'robot-speed': 'speed'
        };

        for (const [elementId, field] of Object.entries(fields)) {
            document.getElementById(elementId).textContent =
                data[field] ?? '—';
        }

        status.textContent = 'Last updated: ' +
            new Date().toLocaleTimeString();

    } catch (error) {
        status.textContent = 'Unable to update robot data';
        console.error('Robot data update failed:', error);
    }
}

updateRobotData();
setInterval(updateRobotData, 2000);
</script>
</body>
</html>


<?php
if (!isset($_FILES['file']) || !is_uploaded_file($_FILES['file']['tmp_name'])) {
	echo 'Please select a file';
} else {
	try {
		$upload = $_FILES['file'];
		$uri = '/files/' . uniqid() . '-' . basename($upload['name']);
		$destination = __DIR__ . $uri;
		move_uploaded_file($upload['tmp_name'], $destination);

		echo 'File was uploaded successfully to ' . $uri;
	} catch (Exception $e) {
		echo 'Sorry, could not upload file';
	}
}

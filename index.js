const IP = '10.40.132.201'
const PORT = 3456
const NGROK_URL = 'https://4936-205-185-105-39.ngrok-free.app'
// async function startCamera() {
//     const constraints = {
//         video: {
//             facingMode: 'environment'
//         }
//     };
//     const stream = await navigator.mediaDevices.getUserMedia(constraints);
//     const video = document.getElementById('video');
//     video.srcObject = stream;
// }

// async function captureImage() {
//     console.log('capturing image');
//     const video = document.getElementById('video');
//     const canvas = document.createElement('canvas');
//     canvas.width = video.videoWidth;
//     canvas.height = video.videoHeight;
//     const context = canvas.getContext('2d');
//     context.drawImage(video, 0, 0, canvas.width, canvas.height);
//     const imageData = canvas.toDataURL('image/png');

//     // Send imageData to server
//     console.log(await fetch(`http://${IP}:${PORT}/upload`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ image: imageData })
//     }));
// }

// document.getElementById('capture').addEventListener('click', captureImage);

// startCamera();


async function startCamera() {
    const constraints = {
        video: {
            facingMode: 'environment' // Use 'user' for front camera
        }
    };

    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        const video = document.getElementById('video');
        video.srcObject = stream;
    } catch (error) {
        console.error("Error accessing camera: ", error);
        alert("Camera access denied or not available. Please check your settings.");
    }
}
var devices
async function captureImage() {
    devices = await navigator.mediaDevices.enumerateDevices()
    // window.alert(devices)
    // console.log(devices)
    for (const i of devices){
        console.log(i)
        console.log(i.getCapabilities())
        console.log(typeof i)
    }

    const video = document.getElementById('video');
    if (!video.srcObject) {
        alert("Camera not started. Please allow camera access.");
        return;
    }

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/png');

    // Send imageData to server
    try {
        console.log('trying to send image');
        // const response = await fetch(`https://${IP}:${PORT}/upload`, {
        const response = await fetch(`${NGROK_URL}/upload`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: imageData })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const result = await response.json();
        console.log("Image sent successfully: ", result);
    } catch (error) {
        console.error("Error sending image: ", error);
        alert(`Failed to send image to server. Please check your network and server. Error: ${error}`);
    }
}

document.getElementById('capture').addEventListener('click', captureImage);

startCamera();

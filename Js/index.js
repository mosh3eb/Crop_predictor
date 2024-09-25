document.getElementById('cropForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  
  const nitrogen = parseFloat(document.getElementById('nitrogen').value) || 0;
  const phosphorus = parseFloat(document.getElementById('phosphorus').value) || 0;
  const potassium = parseFloat(document.getElementById('potassium').value) || 0;
  const temperature = parseFloat(document.getElementById('temperature').value) || 0;
  const humidity = parseFloat(document.getElementById('humidity').value) || 0;
  const ph = parseFloat(document.getElementById('ph').value) || 0;
  const rainfall = parseFloat(document.getElementById('rainfall').value) || 0;

  const data = {
    nitrogen: nitrogen,
    phosphorus: phosphorus,
    potassium: potassium,
    temperature: temperature,
    humidity: humidity,
    ph: ph,
    rainfall: rainfall
  };

  console.log(data);

  document.getElementById('predictionResult').textContent = "Loading...";
  document.getElementById('cropImage').style.display = "none";
  document.getElementById('loadingSpinner').style.display = "block";
  
  try {
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      
      const result = await response.json();
      const predictedCrop = result.predicted_crop;
      document.getElementById('predictionResult').textContent = predictedCrop;
      

      const apiKey = 'WQ34WCE6034k80s2bkaPtNLxvqjFdx8ib7H8O3huQFsuuJZtspC163aq';
      const pexelsResponse = await fetch(`https://api.pexels.com/v1/search?query=${predictedCrop}`, {
        headers: {
          Authorization: apiKey
        }
      });
      const pexelsData = await pexelsResponse.json();
      
      if (pexelsData.photos.length > 0) {
        const imageUrl = pexelsData.photos[0].src.medium;
        const cropImage = document.getElementById('cropImage');
        cropImage.src = imageUrl;
        cropImage.style.display = "inline-block"; 
      } else {
        console.log('No crop images found');
        document.getElementById('predictionResult').textContent += ' (No image available)';
      }
  } catch (error) {
      console.error('Error fetching prediction or image:', error);
      document.getElementById('predictionResult').textContent = "Error fetching data.";
  } finally {
      document.getElementById('loadingSpinner').style.display = "none";

      setTimeout(() => {
          document.getElementById('cropForm').reset();  
          document.getElementById('predictionResult').textContent = '';  
          document.getElementById('cropImage').style.display = "none";  
      }, 60000);
  }
});
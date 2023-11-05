function fetchData() {
    const loader = document.getElementById('loader');
    loader.style.display = 'block';
  
    const videoIdInput = document.getElementById('video_id').value;
    const videoId = extractVideoId(videoIdInput);
  
    fetch('http://localhost:8000/openai/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        video_id: videoId
      })
    })
      .then(response => response.text())
      .then(data => {
        document.getElementById('response').innerHTML = data;
        document.getElementById('response').style.display = 'block';
        loader.style.display = 'none';
      })
      .catch(error => {
        console.error(error);
        loader.style.display = 'none';
      });

      videoIdInput = '';

  }
  
  function extractVideoId(url) {
    const videoIdIndex = url.indexOf('v=') + 2;
    return url.slice(videoIdIndex);
  }
  
  document.getElementById('fetch-button').addEventListener('click', fetchData);
  
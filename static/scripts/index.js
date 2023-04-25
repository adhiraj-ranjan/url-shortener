
function showFlashMessage(message) {
    var flashMessage = document.getElementById('flash-message');
    flashMessage.innerHTML = message;
    flashMessage.style.display = 'block';
    setTimeout(function() {
      flashMessage.style.display = 'none';
    }, 4000); // hide message after n seconds
  }

function copy_to_clip(text){
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            console.log("url copied!")
        }, () => {
            showFlashMessage("Failed to copy");
        });
    } else {
            const textarea = document.createElement('textarea');
            textarea.value = responseJson["url"];
            document.body.appendChild(textarea);
            textarea.select();
            try {
            document.execCommand('copy');
            console.log("url copied!")
            } catch (err) {
                showFlashMessage("Failed to copy");
            }
            document.body.removeChild(textarea);
    }
}
const resultBox = document.querySelector(".result");
document.getElementById("submitForm").addEventListener("submit", function(event) {
        event.preventDefault();

        var longUrl = document.getElementById("long-url").value;
        var alias = document.getElementById("alias").value;
        fetch('/create_short_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'long_url': longUrl, 'alias': alias}),
        })
        .then(response => response.json())
        .then(responseJson => {
            if (responseJson['status'] == "fail"){
                showFlashMessage(responseJson['response']);
            }else{
                resultBox.style.display = "block"
                resultBox.innerHTML = responseJson['url'];
                copy_to_clip(responseJson['url'])
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
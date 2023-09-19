{{video_url|safe}}.forEach(element => {
    let video = document.querySelector('video_display');
    document.querySelector('url').innerHTML = element
    console.log(element)
    video.src = element;
});
function analyzeVideo() {
    let videoUrl = document.getElementById("video_url").value;
    let resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "正在分析，请稍候...";

    fetch("/analyze", {
        method: "POST",
        body: new URLSearchParams({ "video_url": videoUrl }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            resultDiv.innerHTML = `<p><strong>解析结果：</strong> ${data.summary}</p>`;
        } else {
            resultDiv.innerHTML = `<p style="color: red;">分析失败，请检查 URL。</p>`;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `<p style="color: red;">请求错误：${error}</p>`;
    });
}

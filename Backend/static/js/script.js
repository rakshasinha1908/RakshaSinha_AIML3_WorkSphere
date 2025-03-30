async function loadQuestion() {
    try {
      const res = await fetch('/get-question');
      const data = await res.json();
      document.getElementById("question-area").innerText = data.question;
    } catch (error) {
      document.getElementById("question-area").innerText = "⚠️ Failed to load question.";
    }
  }
  
  function logout() {
    window.location.href = "/logout";
  }
  
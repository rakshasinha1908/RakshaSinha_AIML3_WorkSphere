// For question (used in dashboard)
async function loadQuestion() {
  try {
    const res = await fetch('/get-question');
    const data = await res.json();
    document.getElementById("question-area").innerText = data.question;
  } catch (error) {
    document.getElementById("question-area").innerText = "⚠️ Failed to load question.";
  }
}

// For logout (used in all pages)
function logout() {
  window.location.href = "/logout";
}

// On page load - tips + dashboard actions
document.addEventListener("DOMContentLoaded", () => {
  // Random Tip Generator
  const tips = [
    "Hydrate more for better focus 💧",
    "Take a quick walk to declutter your mind 🚶‍♀️",
    "Stretch your body, relax your mind 🧘",
    "Sit upright for better breathing and focus 🪑",
    "Take a deep breath — you've got this 🌬️",
    "Disconnect for 5 mins, then bounce back stronger ⚡"
  ];
  const tipText = document.getElementById("tip-text");
  if (tipText) {
    const randomIndex = Math.floor(Math.random() * tips.length);
    tipText.textContent = tips[randomIndex];
  }

  // Load question if on dashboard
  if (document.getElementById("question-area")) {
    loadQuestion();
  }
});

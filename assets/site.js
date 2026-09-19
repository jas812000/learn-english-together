// Keep the footer copyright year current.
const year = document.getElementById('y');

if (year) {
  year.textContent = new Date().getFullYear();
}

// Play the pronunciation audio associated with a vocabulary button.
document.addEventListener('click', (event) => {
  const button = event.target.closest('.speak');

  if (!button) {
    return;
  }

  const id = button.getAttribute('data-audio');
  const audio = document.getElementById(`audio-${id}`);

  if (!audio) {
    return;
  }

  audio.currentTime = 0;

  // Browser autoplay or media policies can reject playback.
  // Keep the page usable instead of leaving an unhandled promise rejection.
  audio.play().catch(() => {
    // No further action is required when playback is blocked.
  });
});

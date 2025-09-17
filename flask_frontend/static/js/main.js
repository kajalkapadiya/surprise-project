// small confetti implementation
function playConfetti() {
    const root = document.getElementById('confetti-root') || document.body;
    for (let i = 0; i < 40; i++) {
        const d = document.createElement('div');
        d.className = 'confetti';
        d.style.position = 'fixed';
        d.style.left = Math.random() * 100 + '%';
        d.style.top = '-10px';
        d.style.width = '8px';
        d.style.height = '12px';
        d.style.background = `hsl(${Math.random() * 360} 70% 60%)`;
        d.style.opacity = 0.95;
        d.style.transform = `rotate(${Math.random() * 360}deg)`;
        d.style.transition = 'top 2s linear, opacity 2s';
        document.body.appendChild(d);
        // drop it
        setTimeout(() => {
            d.style.top = (100 + Math.random() * 30) + 'vh';
            d.style.opacity = 0;
        }, 50 + Math.random() * 300);
        // cleanup
        setTimeout(() => d.remove(), 2600);
    }
}

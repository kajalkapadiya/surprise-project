// Basic memory match that fetches photos from the API or uses local assets
(async function () {
    // If you want to fetch quiz images from Django API, implement fetch here.
    // For local dev we'll use images placed in static/assets/photos/
    const photos = [
        "photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"
    ];
    // make pairs
    let cards = photos.concat(photos);
    function shuffle(a) { return a.sort(() => Math.random() - 0.5); }
    cards = shuffle(cards);

    const root = document.getElementById('game-root');
    cards.forEach((img, idx) => {
        const c = document.createElement('div');
        c.className = 'card';
        c.dataset.img = img;
        const back = document.createElement('div');
        back.className = 'back';
        back.style.backgroundImage = `url('/static/assets/photos/${img}')`;
        c.appendChild(back);
        c.addEventListener('click', onClickCard);
        root.appendChild(c);
    });

    let flipped = [];
    function onClickCard(e) {
        const card = e.currentTarget;
        if (card.classList.contains('matched') || flipped.indexOf(card) !== -1) return;
        card.classList.add('flipped');
        flipped.push(card);
        if (flipped.length === 2) {
            setTimeout(check, 700);
        }
    }
    function check() {
        const [a, b] = flipped;
        if (a.dataset.img === b.dataset.img) {
            a.classList.add('matched'); b.classList.add('matched');
            // win?
            if (document.querySelectorAll('.matched').length === cards.length) {
                setTimeout(() => alert("You revealed a secret! Check the Letter."), 300);
            }
        } else {
            a.classList.remove('flipped'); b.classList.remove('flipped');
        }
        flipped = [];
    }
})();

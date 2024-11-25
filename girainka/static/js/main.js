document.addEventListener('DOMContentLoaded', () => {
  const cardContainer = document.getElementById('card-container');

  // Sample data for success stories
  const successStories = [
    {
      name: 'Kayigema Peace',
      image: 'https://i.ytimg.com/vi/AJocoZEV7ew/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBLPkc_nG0T2ekch02dQ1ThzrFeyw',
      rating: 4,
      feedback: 'I recently used MilkTrack, and it exceeded all my expectations. The attention to detail and personalized service were outstanding.'
    },
    {
      name: 'Kalisa Tom',
      image: 'https://i.ytimg.com/vi/AJocoZEV7ew/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBLPkc_nG0T2ekch02dQ1ThzrFeyw',
      rating: 5,
      feedback: 'I recently took a trip organized by MilkTrack, and it exceeded all my expectations. The attention to detail and personalized service were outstanding.'
    },
    {
      name: 'MUGABO Sandals',
      image: 'https://i.ytimg.com/vi/AJocoZEV7ew/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBLPkc_nG0T2ekch02dQ1ThzrFeyw',
      rating: 5,
      feedback: 'I recently took a trip organized by MilkTrack, and it exceeded all my expectations. The attention to detail and personalized service were outstanding.'
    }
  ];

  function createStarRating(rating) {
    return '★'.repeat(rating);
  }

  
  successStories.forEach(story => {
    const card = document.createElement('div');
    card.classList.add('card');

    card.innerHTML = `
      <div class="card-item">
        <img src="${story.image}" alt="${story.name}">
        <h3>${story.name}</h3>
        <div class="stars">${createStarRating(story.rating)}</div>
        <p>"${story.feedback}"</p>
      </div> 
    `;

    cardContainer.appendChild(card);
  });
});

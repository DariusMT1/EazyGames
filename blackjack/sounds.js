const suits = ['hearts', 'diamonds', 'spades', 'clubs'];
const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
const cardValues = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
};

let deck, playerHand, dealerHand, playerScore, dealerScore, gameOver;
let playerMoney, currencySymbol, betAmount;

const dealSound = new Audio('sounds/deal.mp3');
const winSound = new Audio('sounds/win.mp3');
const loseSound = new Audio('sounds/lose.mp3');
const tieSound = new Audio('sounds/tie.mp3');

document.getElementById('start-game').addEventListener('click', setupGame);
document.getElementById('place-bet').addEventListener('click', placeBet);
document.getElementById('hit').addEventListener('click', hit);
document.getElementById('stand').addEventListener('click', stand);
document.getElementById('restart').addEventListener('click', startGame);

function setupGame() {
    playerMoney = parseFloat(document.getElementById('money').value);
    currencySymbol = document.getElementById('currency').value;
    document.getElementById('setup').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    updateMoney();
}

function placeBet() {
    betAmount = parseFloat(document.getElementById('bet').value);
    if (betAmount > playerMoney) {
        alert('You cannot bet more than you have!');
        return;
    }
    startGame();
}

function startGame() {
    deck = createDeck();
    shuffleDeck(deck);
    playerHand = [];
    dealerHand = [];
    playerScore = 0;
    dealerScore = 0;
    gameOver = false;

    playerHand.push(dealCard());
    playerHand.push(dealCard());
    dealerHand.push(dealCard());
    dealerHand.push(dealCard());

    updateScores();
    updateUI();
}

function createDeck() {
    let deck = [];
    for (let suit of suits) {
        for (let rank of ranks) {
            deck.push({ suit, rank });
        }
    }
    return deck;
}

function shuffleDeck(deck) {
    for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
    }
}

function dealCard() {
    playSound(dealSound);
    return deck.pop();
}

function calculateScore(hand) {
    let score = 0;
    let hasAce = false;
    for (let card of hand) {
        score += cardValues[card.rank];
        if (card.rank === 'A') {
            hasAce = true;
        }
    }
    if (hasAce && score + 10 <= 21) {
        score += 10;
    }
    return score;
}

function updateScores() {
    playerScore = calculateScore(playerHand);
    dealerScore = calculateScore(dealerHand);
}

function updateUI() {
    document.getElementById('player-cards').innerHTML = '';
    document.getElementById('dealer-cards').innerHTML = '';

    for (let card of playerHand) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card';
        const cardImg = document.createElement('img');
        cardImg.src = `images/${card.rank}_of_${card.suit}.png`;
        cardDiv.appendChild(cardImg);
        document.getElementById('player-cards').appendChild(cardDiv);
    }

    for (let card of dealerHand) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card';
        const cardImg = document.createElement('img');
        cardImg.src = `images/${card.rank}_of_${card.suit}.png`;
        cardDiv.appendChild(cardImg);
        document.getElementById('dealer-cards').appendChild(cardDiv);
    }

    document.getElementById('player-score').textContent = `Score: ${playerScore}`;
    document.getElementById('dealer-score').textContent = `Score: ${dealerScore}`;
    updateMoney();

    if (gameOver) {
        document.getElementById('hit').disabled = true;
        document.getElementById('stand').disabled = true;
    } else {
        document.getElementById('hit').disabled = false;
        document.getElementById('stand').disabled = false;
    }

    if (playerScore > 21) {
        document.getElementById('message').textContent = 'You busted! Dealer wins.';
        playerMoney -= betAmount;
        playSound(loseSound);
        gameOver = true;
    } else if (dealerScore > 21) {
        document.getElementById('message').textContent = 'Dealer busted! You win.';
        playerMoney += betAmount;
        playSound(winSound);
        gameOver = true;
    } else if (gameOver) {
        if (playerScore > dealerScore) {
            document.getElementById('message').textContent = 'You win!';
            playerMoney += betAmount;
            playSound(winSound);
        } else if (playerScore < dealerScore) {
            document.getElementById('message').textContent = 'Dealer wins.';
            playerMoney -= betAmount;
            playSound(loseSound);
        } else {
            document.getElementById('message').textContent = 'It\'s a tie!';
            playSound(tieSound);
        }
    } else {
        document.getElementById('message').textContent = '';
    }
}

function updateMoney() {
    document.getElementById('player-money').textContent = `Money: ${currencySymbol}${playerMoney.toFixed(2)}`;
}

function hit() {
    if (!gameOver) {
        playerHand.push(dealCard());
        updateScores();
        updateUI();
        if (playerScore > 21) {
            gameOver = true;
            updateUI();
        }
    }
}

function stand() {
    if (!gameOver) {
        while (dealerScore < 17) {
            dealerHand.push(dealCard());
            updateScores();
        }
        gameOver = true;
        updateUI();
    }
}

function playSound(sound) {
    sound.currentTime = 0;
    sound.play();
}

startGame();

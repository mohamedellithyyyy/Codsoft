// Get the input field
const inputField = document.querySelector('.screen input');

// Get all the buttons
const buttons = document.querySelectorAll('.buttons button');

// Add click event listeners to each button
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Get the button's text content
        const buttonText = button.textContent;

        // Handle different button clicks
        if (buttonText === '=') {
            // Evaluate the expression and display the result
            try {
                const result = eval(inputField.value);
                inputField.value = result;
            } catch (error) {
                inputField.value = 'Error';
            }
        } else {
            // Append the button's text content to the input field
            inputField.value += buttonText;
        }
    });
});

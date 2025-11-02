document.addEventListener('DOMContentLoaded', () => {
    const ayushInput = document.getElementById('ayushInput');
    const searchButton = document.getElementById('searchButton');
    const resultsDiv = document.getElementById('results');

    const search = async () => {
        const term = ayushInput.value.trim();
        if (!term) {
            resultsDiv.innerHTML = 'Please enter an AYUSH term.';
            return;
        }

        resultsDiv.innerHTML = 'Fetching mapping...';

        try {
            const response = await fetch(`/map-namaste/${term}`);
            
            if (response.ok) {
                const data = await response.json();
                resultsDiv.innerHTML = `
                    <strong>NAMASTE Term:</strong> ${data.namaste_term} (${data.namaste_code})<br>
                    <strong>ICD-11 Title:</strong> ${data.icd11_title}<br>
                    <strong>ICD-11 Code:</strong> ${data.icd11_code}<br>
                    <strong>ICD-11 Definition:</strong> ${data.icd11_definition || 'N/A'}<br>
                    <br>
                    <em>(ICD-11 details fetched live from WHO API)</em>
                `;
            } else {
                const errorData = await response.json();
                resultsDiv.innerHTML = `Error: ${errorData.detail || response.statusText}`;
            }
        } catch (error) {
            resultsDiv.innerHTML = 'Failed to connect to the server. Is the backend running?';
        }
    };

    searchButton.addEventListener('click', search);
    ayushInput.addEventListener('keyup', (event) => {
        if (event.key === 'Enter') {
            search();
        }
    });
});
async function predictPrice() {
    const km = document.getElementById("km").value;
    const result = document.getElementById("result");

    if (!km) {
        result.innerHTML = "Please enter kilometers!";
        return;
    }

    // Sending POST request to Django API
    const response = await fetch("http://127.0.0.1:8000/api/predict/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ km: parseFloat(km) }),
    });

    const data = await response.json();

    if (response.ok) {
        result.innerHTML = `Predicted Price: $${data.predicted_price.toFixed(2)}`;
    } else {
        result.innerHTML = "Error: " + data.error;
    }
}

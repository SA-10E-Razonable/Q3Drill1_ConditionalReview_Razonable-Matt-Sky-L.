from pyscript import document

def show_results():
    # Get the "View Results" div
    div = document.getElementById("view-results")

    # Try reading the input values
    try:
        energy = float(document.getElementById("bar-energy").value)
        tempo = float(document.getElementById("bar-tempo").value)
    except ValueError:
        set_result(div, "Please enter valid numbers!")
        return

    # Check ranges
    if energy < 0 or energy > 100 or tempo < 0 or tempo > 100:
        set_result(div, "Values must be between 0 and 100!")
        return

    # Calculate beat
    beat = (energy + tempo) / 2

    # Determine style
    if beat <= 40:
        style = "Chill / Lo-Fi 🎧"
    elif beat <= 70:
        style = "Pop 🎵"
    elif beat <= 90:
        style = "Rock 🔥"
    else:
        style = "EDM ⚡"

    # Show result below the button
    set_result(div, f"You match the beat: {style}")


def set_result(button_div, text):
    """
    Helper function to create or update the result div below the button
    """
    # Check if a result div already exists
    result_div = button_div.nextElementSibling
    if result_div is None or result_div.id != "result":
        # Create it if it doesn't exist
        result_div = document.createElement("div")
        result_div.id = "result"
        result_div.style.color = "#c24b3b"
        result_div.style.fontWeight = "bold"
        result_div.style.fontSize = "2rem"
        result_div.style.marginTop = "10px"
        button_div.parentNode.insertBefore(result_div, button_div.nextSibling)

    result_div.innerText = text




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade Calculator</title>
    <style>

        body {
            font-family: Arial, sans-serif;
            margin: 0; 
            height: 100vh; 
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: beige; 
        }

   
        .container {
            background-color: white; 
            padding: 20px;          
            border-radius: 10px;     
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
            max-width: 500px;      
            width: 100%;             
            box-sizing: border-box;
        }

        h1 {
            color: #333;
        }

        input, button {
            margin: 10px 0;
            padding: 5px;
            width: 100%;            
            box-sizing: border-box;   
        }

        .message {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Grade Calculator</h1>

        <form id="gradeForm">
            <label>Prelim Grade:</label>
            <input type="text" id="prelim" placeholder="Enter your Prelim grade">
            <button>Calculate</button>
        </form>

        <div id="resultMessage" class="message"></div>
    </div>

    <script>
        document.getElementById('gradeForm').onsubmit = function(event) {
            event.preventDefault();

            var prelimGrade = parseFloat(document.getElementById('prelim').value);
            var message = "";

            if (isNaN(prelimGrade) || prelimGrade < 0 || prelimGrade > 100) {
                message = "Please enter a valid grade between 0 and 100.";
            } else if (prelimGrade >= 90) {
                message = "You've already passed with a Prelim grade of " + prelimGrade + ". You are also qualified for Dean's Lister!";
            } else if (prelimGrade >= 60 && prelimGrade < 90) {
                var requiredMidterm = ((75 - (prelimGrade * 0.2)) / 0.8) * 0.3;
                var requiredFinal = ((75 - (prelimGrade * 0.2)) / 0.8) * 0.5;

                message = "To pass, you need at least " + requiredMidterm.toFixed(2) + " in Midterms and " + requiredFinal.toFixed(2) + " in Finals.";
            } else if (prelimGrade < 60) {
                message = "Unfortunately, with a Prelim grade of " + prelimGrade + ", it is difficult to pass.";
            }

            document.getElementById('resultMessage').innerText = message;
        };
    </script>

</body>
</html>

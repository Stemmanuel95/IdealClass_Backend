@REM rem Run tests (replace with your actual test command)
@REM rem npm test

@REM rem Start the server and check for errors
@REM npm run start & ...... start command is : "start": "node app.js"

@REM rem Wait for server to start (adjust timeout if needed)
@REM timeout /t 5 /nobreak > NUL

@REM rem Check for successful response (adjust URL and expected output)
@REM curl http://localhost:5000/ > NUL && (
@REM   echo Server started successfully!
@REM ) || (
@REM   echo Server startup failed! Fix errors before pushing.
@REM   exit /b 1
@REM )

@REM rem Stop the server (optional, adjust based on your needs)
@REM taskkill /F /IM node.exe

@REM exit /b 0

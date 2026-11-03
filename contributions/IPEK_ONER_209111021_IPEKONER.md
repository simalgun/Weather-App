# Personal Contribution

Name: İpek Öner  
Student ID:2409111021
GitHub Username: ipekonerr

## Contributions

I was responsible for the state management part of the weather application in `state.py`.

My contributions include:

- Implemented `load_state()` to read the previous rain result from a JSON file.
- Implemented `save_state()` to save the latest rain result.
- Created `should_notify()` to send an alert only when rain becomes newly expected.
- Added error handling for missing or invalid saved data.

## Technical Details

The implementation uses Python functions, JSON data, file operations, and conditional statements. The saved state helps the app remember the previous result and avoid sending repeated notifications.

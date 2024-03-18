A small assignment for demonstrating your working knowledge of automated web user interface testing and ensuring quality.

The provided application is a simple demo application for managing contacts. You can run it by executing `npm install` inside of the directory and then run the `npm run dev` command to execute the application. Then you should be able to access it under localhost:4000. The demo user is:

Username: test
Password: test

Your task is to create tests in organized manner that validate the functionality and do some manual testing to ensure quality.

Automated Tests Assignment:

1.) Please familiarize yourself with Playwright (https://playwright.dev/docs/intro) and its features and integrate it into the provided project by replacing the `PLACEHOLDER` of the `test` script command in the package.json file, so we can execute your tests simply by running `npm run test`. Please put your test inside of the `tests` subdirectory. 

2.) Use the Playwright API to create automated tests for the following use cases:

- Sign in into the Application
- Create a new Contact
- Update a Contact
- Delete a Contact
- Filter Contacts
- (Optionally) Sign out of the Application
- (Optionally) Favorize Contact

Manual Tests Assignment:

The provided app contains some intended bugs that you are supposed to find. This bugs simulate some realistic cases that can happen in a day to day work, but they are designed in a way so they do not prevent you from fulfilling the automated tests assignment. Please try to find them and document everything you can find with sufficient detail in the Notes.md file inside of the root directory.

When you are done, please remove the node_modules directory and send us the project as a zip file via e-mail for later evaluation.

Thank you and good luck!

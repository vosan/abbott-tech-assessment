# abbott-tech-assessment
This is the tech assessment from candidate Volodymyr Burmitskyi.

This project is built using Python 3 and Behave.

All BDD scenarios are located in 'features' directory. 
Step implementations can be found in 'steps' directory.
Page objects are located in 'pages' directory.

Ro run the tests execute the following command:
`behave -D user_email=codechallengeadc@gmail.com -D user_password=P@ssword1234 -D country=US -D language=en_US`

In the above command you can configure the parameters.

You can also simply run `behave` and it will run the tests with the default set of parameters (parameters in the above command are the default parameters).

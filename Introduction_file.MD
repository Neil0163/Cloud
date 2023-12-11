Here are some key terms for this module.

Deployment
The process of taking some software that is running on your computer and making it run on the Internet where it is accessible to other people. For this, you will typically also try to make it a bit more robust.

Abstraction
The process of hiding or ignoring the details of something in order to focus on the important parts. For example, when you drive a car, you don't need to know precisely how the engine works. Those details are abstracted. This is achieved through an abstraction layer — the controls for the car that allow you to ignore the details of the engine.

Cloud Computing
To understand this term it is best to compare it to the alternative. In the past, if you wanted to run a program you would have to buy all of the physical computers that you would need in order to run it, set them up, probably connect them to the Internet, and maintain them yourself. If you needed the servers for only a few weeks, you still had to buy them outright, and then hopefully sell them to someone else. This is typically called on-premise computing.

In Cloud Computing, you go to a cloud provider company like Amazon Web Services (AWS) and say "I've packaged up my web application into this file — can you run between 2 and 12 copies of it depending on how many are needed to serve the traffic it is getting." And AWS will go and do that. It's a bit more complex than that in practice, but that is the general idea.

Cloud computing as a way of abstracting away the details of the physical machinery that you need to run your program. The abstraction layer can vary according to the problem being solved, but often involves creating virtual computers and connecting them with virtual connections. The cloud provider then handles the details of how to implement that.

CI-CD
This stands for Continuous Integration (CI) and Continuous Deployment (CD).

Continuous Integration is a process where an engineer pushes their code to a repository, a cloud system then downloads the code and runs some tests to check whether it is suitable for going into the main codebase. These tests typically include running the automated tests written by the developer, but may also include other tests for code style, test coverage, or security testing.

Continuous Deployment is a process where after these tests are run the software is automatically deployed — typically to a cloud system.
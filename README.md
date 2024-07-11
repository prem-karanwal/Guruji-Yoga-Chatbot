**Guruji - Your Virtual Yoga Mentor**

## Inspiration

The inspiration for creating Guruji came from the desire to promote physical and mental well-being through the practice of yoga. With the increasing popularity of yoga and its proven benefits, we wanted to create a virtual assistant that could make yoga more accessible and personalized. The goal was to provide users with a reliable and knowledgeable guide who could assist them with yoga-related queries, recommend asanas for specific issues, and help them maintain a consistent yoga practice.

## Development Process

### Technologies Used

- **Frontend:** The frontend of Guruji was built using React to create a responsive and interactive user interface.
- **Backend:** The backend was developed using Flask, a lightweight Python web framework, to handle API requests and manage the chat session.
- **AI Model:** We used Google's Generative AI model to power the chatbot, allowing it to provide accurate and helpful responses to user queries.

### Steps Taken

1. **Initial Planning:** We started by outlining the key features and functionalities of the chatbot, including the ability to handle user queries, capture user information, and provide personalized yoga recommendations.
2. **Model Integration:** We integrated the Generative AI model from Google to enable the chatbot to generate responses based on user input.
3. **Frontend Development:** Using React, we developed the user interface, ensuring it was clean, intuitive, and responsive.
4. **Backend Development:** We set up the Flask backend to handle incoming requests from the frontend, communicate with the AI model, and return responses.
5. **CORS Handling:** We addressed cross-origin resource sharing (CORS) issues to ensure smooth communication between the frontend and backend.
6. **Testing and Iteration:** We tested the chatbot extensively, gathering feedback and making improvements to enhance the user experience and ensure accurate responses.

### Challenges Faced

- **API Key Management:** Initially, we faced issues with managing the API key securely and ensuring it was correctly configured in the environment.
- **CORS Issues:** Handling CORS was a significant challenge, but we resolved it by properly configuring the Flask-CORS library.
- **Response Formatting:** Ensuring that the chatbot's responses were well-formatted and clear, especially when providing lists or bullet points, required careful attention.
- **User Interaction:** Designing the chatbot to capture user information (name and email) before answering queries required thoughtful implementation to maintain a smooth user experience.

## Conclusion

Developing Guruji was a rewarding experience that allowed us to combine our interests in AI, web development, and wellness. The project not only enhanced our technical skills but also provided a meaningful tool that can help users incorporate yoga into their daily lives. We are excited about the potential of Guruji to make a positive impact and look forward to continuing to improve and expand its capabilities.

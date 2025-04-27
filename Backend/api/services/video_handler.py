from google import genai
from google.genai import types


class VideoHandler():
    client = genai.Client(api_key="AIzaSyAALehML5GdQAU6ed-ADJ82qOGBidt1wT4")

    def Response(self, videoName):
        video_file_name = f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/videos/{videoName}"
        video_bytes = open(video_file_name, 'rb').read()

        response = self.client.models.generate_content(
            model='models/gemini-2.0-flash',
            contents=types.Content(
                parts=[
                    types.Part(
                        inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
                    ),
                    types.Part(text='''
                               Analyze the provided video. Based SOLELY on the visual patterns you detect, Generate a personalized 7-day diet plan based on the following user body shape and fat.
                    The table should have the following columns in this exact order: Day, Breakfast, Lunch, Dinner, Snacks.

                    Structure the response as a complete HTML `<table>` element, including `<thead>` for headers and `<tbody>` for the rows.

                    Output ONLY the HTML `<table>` element and its full content. Do not include any surrounding text, markdown code blocks (like ```html), or any other characters before or after the HTML table code.

                    Example structure of the HTML you should generate (use the actual meal plan data for the content):

                    ```html
                    <table>
                    <thead>
                        <tr>
                        <th>Day</th>
                        <th>Breakfast</th>
                        <th>Lunch</th>
                        <th>Dinner</th>
                        <th>Snacks</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <td>Monday</td>
                        <td>[Monday Breakfast content]</td>
                        <td>[Monday Lunch content]</td>
                        <td>[Monday Dinner content]</td>
                        <td>[Monday Snacks content]</td>
                        </tr>
                        <tr>
                        <td>Tuesday</td>
                        <td>[Tuesday Breakfast content]</td>
                        <td>[Tuesday Lunch content]</td>
                        <td>[Tuesday Dinner content]</td>
                        <td>[Tuesday Snacks content]</td>
                        </tr>
                        <!-- ... and so on for other days -->
                    </tbody>
                    </table>
                    '''
                    '''Output Requirements:
                    IMPORTANT: 
                    NEVER use markdown formatting, code blocks (` ``` `), or escape sequences like `\n`.
                    Provide the requested information directly without conversational filler..
                    Begin the output now:''')
                ]
            )
        )
        return response.text
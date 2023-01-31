import { useHistory } from "react-router-dom"

import NewMeetupForm from "../components/meetups/NewMeetupForm"

function NewMeetupPage() {
  const history = useHistory()

  function addMeetupHandler(meetupData) {
    fetch(
      "https://react-getting-started-71aaa-default-rtdb.firebaseio.com/meetups.json",
      {
        method: "POST",
        body: JSON.stringify(meetupData),
        headers: {
          "Content-Type": "application/json",
        },
      }).then(() => {
				// history.push()를 사용하면 스택을 쌓는거라 이전 페이지로 돌아가기 가능
				// 양식이 제출되는 경우는 의미가 없으므로 replace가 적당
				history.replace('/');
			}
    )
  }

  return (
    <section>
      <h1>Add New Meetup</h1>
      <NewMeetupForm onAddMeetup={addMeetupHandler}></NewMeetupForm>
    </section>
  )
}

export default NewMeetupPage

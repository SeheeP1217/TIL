import { Route, Switch } from "react-router-dom"

import AllMeetupsPage from "./pages/AllMeetups"
import FavoritesPage from "./pages/Favorites"
import NewMeetupPage from "./pages/NewMeetup"

function App() {
  // localhost:3000/
  // my-page.com/
  return (
    <div>
      <Switch>
        <Route path="/" exact={true}>
          <AllMeetupsPage />
        </Route>
        <Route path="/new-meetup">
          <NewMeetupPage />
        </Route>
        <Route path="/favorites">
          <FavoritesPage />
        </Route>
      </Switch>
    </div>
  )
}

export default App

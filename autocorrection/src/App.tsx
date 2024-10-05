import AutocorrectTextarea from './autocorrect'
import './App.css'
function App() {

  return (
    <div className="App">
      <AutocorrectTextarea corrections={{
        'realy': 'really',
        'wierd': 'weird',
      }} />
    </div>
  )
}

export default App

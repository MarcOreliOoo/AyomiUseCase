import React from 'react'
import { Button } from './ui/button';

const Calculator = () => {
	const [counter, setCounter] = React.useState(0);
  return (
	<div>
		<h1>{counter}</h1>
		<Button variant="default" onClick={() => setCounter(prev => prev+1)}>
			Increment
		</Button>
	</div>
  )
}

export default Calculator
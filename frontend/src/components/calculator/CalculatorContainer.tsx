import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";

import Calculator from "./Calculator";
import TooltipAccordion from "./TooltipRPN";
import { URL_TO_FETCH } from "@/lib/utils";

const CalculatorContainer = () => {
    const [calculationRes, setCalculationRes] = useState("");

    const [inputValue, setInputValue] = useState("");
    const [expression, setExpression] = useState("");

    const handleCalcul = async () => {
        if (expression.trim() === "") return;
        try {
            const finalExpression = { expression: expression.trim() };
            const response = await fetch(`${URL_TO_FETCH}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(finalExpression),
            });
            const data = await response.json();
            setCalculationRes(data.result);
        } catch (error) {
            console.error(error);
        }
    };

    const handleClear = () => {
        setExpression("");
        setInputValue("");
        setCalculationRes("");
    };

    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex flex-row items-center justify-between">RPN Calculator</CardTitle>
                <div className="text-sm text-muted-foreground">
                    An RPN (Reverse Polish Notation) calculator is a type of calculator that uses postfix notation for
                    mathematical operations.
                    <TooltipAccordion />
                </div>
            </CardHeader>
            <CardContent>
                <Calculator
                    expression={expression}
                    setExpression={setExpression}
                    inputValue={inputValue}
                    setInputValue={setInputValue}
                />
                <Result result={calculationRes} />
            </CardContent>
            <CardFooter className="flex justify-between">
                <Button variant="outline" onClick={handleClear}>
                    Clear
                </Button>
                <Button onClick={handleCalcul}>Calcul</Button>
            </CardFooter>
        </Card>
    );
};

const Result = ({ result }: { result: string }) => {
    return (
        <div className="mt-3 flex w-full flex-row items-start justify-center gap-3">
            <span className="flex h-full min-h-9 w-20 items-center justify-start">Result:</span>
            <span className="flex h-full min-h-9 w-full flex-grow items-center overflow-auto rounded-md border border-input/10 bg-primary/10 px-3 py-1 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50">
                {result}
            </span>
        </div>
    );
};

export default CalculatorContainer;

import React, { useRef } from "react";
import { Input } from "@/components/ui/input";
import { isValidInput } from "@/lib/utils";

type CalculatorProps = {
    expression: string;
    setExpression: React.Dispatch<React.SetStateAction<string>>;
    inputValue: string;
    setInputValue: React.Dispatch<React.SetStateAction<string>>;
};

const Calculator = ({ expression, setExpression, inputValue, setInputValue }: CalculatorProps) => {
    const expressionRef = useRef<HTMLSpanElement>(null);

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        event.preventDefault();
        const input = event.target.value;

        if (isValidInput(input)) {
            setInputValue(input);
        } else {
            setInputValue("");
        }
    };

    const handleValidChange = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === "Enter") {
            setExpression((prev) => prev + inputValue + " ");
            setInputValue("");
            if (expressionRef.current) {
                expressionRef.current.scrollLeft = expressionRef.current.scrollWidth;
            }
        }
    };

    return (
        <div className="mx-auto flex max-w-3xl flex-row items-start justify-between gap-3">
            <Input
                placeholder="Write a number or operator and press enter"
                onChange={handleInputChange}
                onKeyDown={handleValidChange}
                className=" w-1/2"
                value={inputValue}
            />
            <span
                ref={expressionRef}
                className="flex h-full min-h-9 w-1/2 flex-grow items-center overflow-auto rounded-md border border-input/10 bg-primary/10 px-3 py-1 text-right text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
            >
                {expression}
            </span>
        </div>
    );
};

export default Calculator;

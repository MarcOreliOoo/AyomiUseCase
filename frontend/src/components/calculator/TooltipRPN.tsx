import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

const TooltipAccordion = () => {
    return (
        <Accordion type="single" collapsible className="w-full">
            <AccordionItem value="item-1">
                <AccordionTrigger>How does it work?</AccordionTrigger>
                <AccordionContent>
                    It operates on a stack. Numbers are pushed onto the stack.
                    <br /> Operations operate on the last one or two numbers in the stack, replacing them with the
                    result.
                    <br />
                    <span>3 5 * = 15</span>
                </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-2">
                <AccordionTrigger>Define your expression in 2 ways</AccordionTrigger>
                <AccordionContent className="flex flex-col gap-2">
                    <span>Choice 1</span>
                    <ul>
                        <li>1. Enter a number and press enter to push it to the stack.</li>
                        <li>2. Enter another number and press enter to push it to the stack.</li>
                        <li>3. Enter an operator and press enter to perform the operation on the last two numbers</li>
                        <li>4. Continue as long as you want... then press Calcul button</li>
                    </ul>
                    <span>Choice 2</span>
                    <ul>
                        <li>
                            1. Enter numbers, space, numbers, blank, operators... and press enter to push it to the
                            stack.
                        </li>
                        <li>2. Continue as long as you want... then press Calcul button</li>
                    </ul>
                </AccordionContent>
            </AccordionItem>
        </Accordion>
    );
};

export default TooltipAccordion;

import DownloadComp from "./Download";
import { ModeToggle } from "./mode-toogle";

const Header = () => {
    return (
        <header>
            <nav className="flex flex-wrap items-center justify-between p-6">
                <div className="mr-6 flex flex-shrink-0 items-center">
                    <a href="/" className="text-xl font-semibold tracking-tight">
                        RPN Calculator
                    </a>
                </div>
                <div className="flex flex-row items-center justify-between gap-x-2">
                    <DownloadComp />
                    <ModeToggle />
                </div>
            </nav>
        </header>
    );
};

export default Header;

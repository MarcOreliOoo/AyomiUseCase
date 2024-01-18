import { Download } from "lucide-react";
import { Button } from "../ui/button";

const DownloadComp = () => {
    const handleDownload = async () => {
        try {
            const response = await fetch("http://localhost:8000/rpn/history");
            console.log(response);
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            window.open(url);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <Button variant="outline" size="icon" onClick={handleDownload}>
            <Download className="h-[1.2rem] w-[1.2rem]" />
        </Button>
    );
};

export default DownloadComp;

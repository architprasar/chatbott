import AboutSectionOne from "@/components/About/AboutSectionOne";
import AboutSectionTwo from "@/components/About/AboutSectionTwo";
import Breadcrumb from "@/components/Common/Breadcrumb";

import { Metadata } from "next";

export const metadata: Metadata = {
  title: "About Page | Genverse Studios",
  description: "This is About Page for Startup Nextjs Template",
  // other metadata
};

const AboutPage = () => {
  return (
    <>
      <Breadcrumb
        pageName="About Page"
        description="Our company is dedicated to providing cutting-edge solutions across various industries. From e-commerce chatbots that boost conversions and offer intelligent product assistance to educational chatbots facilitating context-based problem-solving and document references, we strive to enhance user experiences and drive success. Additionally, our service-based chatbots offer versatile functionalities adaptable to diverse industry needs, providing tailored solutions for customer support, automation, and industry-specific requirements. With a team ready to cater to your needs and deliver exceptional services, we are committed to empowering your vision and exceeding expectations. Let's collaborate to achieve your goals and ensure mutual success."
      />
      <AboutSectionOne />
      {/* <AboutSectionTwo /> */}
    </>
  );
};

export default AboutPage;

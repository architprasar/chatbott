import React, { useEffect, useState, useRef } from 'react';
import './App.css';
import './style.css';
import { SendOutlined } from '@ant-design/icons';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

function Message(props) {
  return (
    <div className={props.sender ? 'message_container message_container_sender' : 'message_container'}>
      <div className='message_info'></div>
      <div className={props.sender ? 'message_box message_box_sender' : 'message_box'}>
        {props.isCarousel ? props.children : <ReactMarkdown>{props.children}</ReactMarkdown>}
      </div>
    </div>
  );
}

function Head() {
  return (
    <div className="head">
      <div className="company_icon"><div className="company_avatar"></div></div>
      <div className="company_name">Fashion bot</div>
      <div className="close_chatbot">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#667085" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="feather feather-x"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </div>
    </div>
  );
}

function Footer() {
  return (
    <div className="footer">
      Powered by <b>&nbsp;ChatGpt-4o</b>
    </div>
  );
}

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <div className="product-name">{product.title}</div>
      <div className="product-rating">{product.rating}</div>
      <div className="product-price">{product.price}</div>
      <button className="product-button" onClick={() => window.open(product.url, '_blank')}>
        View Product
      </button>
    </div>
  );
}

function ProductCarousel({ data }) {
  const settings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 3, // Adjust to show the number of products you want visible
    slidesToScroll: 1,
    arrows: true,
    adaptiveHeight: true
  };

  return (
    <Slider {...settings}>
      {data && data.map((product, idx) => (
        <div key={idx}>
          <ProductCard key={idx} product={product} />
        </div>
      ))}
    </Slider>
  );
}

function MessageBox({ msgs, messagesEndRef }) {
  return (
    <div className="bot_msg_body">
      {msgs.length > 0 && msgs.map((msg, index) => {
        console.log(msg.content);
        if (msg.type === "user") {
          return <Message key={index} sender={true}>{msg.content}</Message>;
        } else if (msg.type === "bot") {
          return <Message key={index}>{msg.content}</Message>;
        } 
        return null;
      })}
      <div ref={messagesEndRef} />
    </div>
  );
}

function MessageInputBox({ msgs, setMsgs }) {
  const [inp, setInp] = useState("");

  const sendMessage = async () => {
    if (inp.trim() === "") return;

    const newMsgs = [...msgs, { type: "user", content: inp }];
    setMsgs(newMsgs);
    setInp("");

    try {
      const res = await axios.get("http://127.0.0.1:8000/generate?k=" + inp);
      console.log(res);
      const botMessage = { type: "bot", content: res.data.response.chat };
      let updatedMsgs = [...newMsgs, botMessage];

      if (res.data.response.function_data) {
        const carouselMessage = { type: "carousel", content: res.data.response.function_data };
        console.log(carouselMessage);
        updatedMsgs = [...updatedMsgs, carouselMessage];
      }
      setMsgs([...updatedMsgs]);
    } catch (error) {
      console.error("Error fetching response:", error);
    }
  };

  return (
    <div className="bot_msg_box">
      <input
        type="text"
        value={inp}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
        onChange={(e) => {
          setInp(e.target.value);
        }}
        className="bot_msg_box_input"
        placeholder='Send message...'
      />
      <button className='bot_msg_box_send' onClick={sendMessage}>
        <SendOutlined />
      </button>
    </div>
  );
}

function Body() {
  const [msgs, setMsgs] = useState([]);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [msgs]);

  return (
    <div className="bot">
      <MessageBox msgs={msgs} messagesEndRef={messagesEndRef}></MessageBox>
      <MessageInputBox msgs={msgs} setMsgs={setMsgs}></MessageInputBox>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <Head></Head>
      <Body></Body>
      <Footer></Footer>
    </div>
  );
}

export default App;

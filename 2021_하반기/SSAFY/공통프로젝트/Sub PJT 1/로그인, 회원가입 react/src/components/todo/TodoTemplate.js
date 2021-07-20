import React from 'react';
import './TodoTemplate.css';

function TodoTemplate({ children }) {
  return (
    <div>
      <div className="TemplateBlock">
        { children }
      </div>
      {/* TodoTemplat에 자식컴포넌트가 생기면 TemplateBlock 사이에 넣어라 */}
    </div>

  )
}


export default TodoTemplate;


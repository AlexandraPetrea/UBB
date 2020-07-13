namespace lab4_cs
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.MatPanel1 = new System.Windows.Forms.Panel();
            this.MatPanel2 = new System.Windows.Forms.Panel();
            this.MatPanel3 = new System.Windows.Forms.Panel();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.ResultPanel = new System.Windows.Forms.Panel();
            this.GenerateBtn = new System.Windows.Forms.Button();
            this.MulBtn = new System.Windows.Forms.Button();
            this.TimeTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.ThreadRButton = new System.Windows.Forms.RadioButton();
            this.NThreadRButton = new System.Windows.Forms.RadioButton();
            this.SuspendLayout();
            // 
            // MatPanel1
            // 
            this.MatPanel1.Location = new System.Drawing.Point(12, 86);
            this.MatPanel1.Name = "MatPanel1";
            this.MatPanel1.Size = new System.Drawing.Size(169, 111);
            this.MatPanel1.TabIndex = 0;
            // 
            // MatPanel2
            // 
            this.MatPanel2.Location = new System.Drawing.Point(204, 86);
            this.MatPanel2.Name = "MatPanel2";
            this.MatPanel2.Size = new System.Drawing.Size(169, 111);
            this.MatPanel2.TabIndex = 1;
            // 
            // MatPanel3
            // 
            this.MatPanel3.Location = new System.Drawing.Point(396, 86);
            this.MatPanel3.Name = "MatPanel3";
            this.MatPanel3.Size = new System.Drawing.Size(169, 111);
            this.MatPanel3.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(187, 133);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(11, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "*";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(379, 133);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(11, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "*";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(571, 133);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(13, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "=";
            // 
            // ResultPanel
            // 
            this.ResultPanel.Location = new System.Drawing.Point(590, 86);
            this.ResultPanel.Name = "ResultPanel";
            this.ResultPanel.Size = new System.Drawing.Size(169, 111);
            this.ResultPanel.TabIndex = 2;
            // 
            // GenerateBtn
            // 
            this.GenerateBtn.Location = new System.Drawing.Point(348, 203);
            this.GenerateBtn.Name = "GenerateBtn";
            this.GenerateBtn.Size = new System.Drawing.Size(75, 23);
            this.GenerateBtn.TabIndex = 5;
            this.GenerateBtn.Text = "Generate";
            this.GenerateBtn.UseVisualStyleBackColor = true;
            this.GenerateBtn.Click += new System.EventHandler(this.GenerateBtn_Click);
            // 
            // MulBtn
            // 
            this.MulBtn.Location = new System.Drawing.Point(348, 57);
            this.MulBtn.Name = "MulBtn";
            this.MulBtn.Size = new System.Drawing.Size(75, 23);
            this.MulBtn.TabIndex = 6;
            this.MulBtn.Text = "Mul";
            this.MulBtn.UseVisualStyleBackColor = true;
            this.MulBtn.Click += new System.EventHandler(this.MulBtn_Click);
            // 
            // TimeTextBox
            // 
            this.TimeTextBox.Location = new System.Drawing.Point(659, 203);
            this.TimeTextBox.Name = "TimeTextBox";
            this.TimeTextBox.Size = new System.Drawing.Size(100, 20);
            this.TimeTextBox.TabIndex = 7;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(623, 206);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(30, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Time";
            // 
            // ThreadRButton
            // 
            this.ThreadRButton.AutoSize = true;
            this.ThreadRButton.Location = new System.Drawing.Point(305, 232);
            this.ThreadRButton.Name = "ThreadRButton";
            this.ThreadRButton.Size = new System.Drawing.Size(68, 17);
            this.ThreadRButton.TabIndex = 9;
            this.ThreadRButton.TabStop = true;
            this.ThreadRButton.Text = "1 Thread";
            this.ThreadRButton.UseVisualStyleBackColor = true;
            // 
            // NThreadRButton
            // 
            this.NThreadRButton.AutoSize = true;
            this.NThreadRButton.Location = new System.Drawing.Point(396, 232);
            this.NThreadRButton.Name = "NThreadRButton";
            this.NThreadRButton.Size = new System.Drawing.Size(73, 17);
            this.NThreadRButton.TabIndex = 10;
            this.NThreadRButton.TabStop = true;
            this.NThreadRButton.Text = "n Threads";
            this.NThreadRButton.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(792, 278);
            this.Controls.Add(this.NThreadRButton);
            this.Controls.Add(this.ThreadRButton);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.TimeTextBox);
            this.Controls.Add(this.MulBtn);
            this.Controls.Add(this.GenerateBtn);
            this.Controls.Add(this.ResultPanel);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.MatPanel2);
            this.Controls.Add(this.MatPanel3);
            this.Controls.Add(this.MatPanel1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel MatPanel1;
        private System.Windows.Forms.Panel MatPanel2;
        private System.Windows.Forms.Panel MatPanel3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Panel ResultPanel;
        private System.Windows.Forms.Button GenerateBtn;
        private System.Windows.Forms.Button MulBtn;
        private System.Windows.Forms.TextBox TimeTextBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.RadioButton ThreadRButton;
        private System.Windows.Forms.RadioButton NThreadRButton;
    }
}
